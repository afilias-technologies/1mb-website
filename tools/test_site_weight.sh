#!/bin/sh
echo "Payload\tHeaders\tTotal\tKB\tCode\tFinal URL"

cat site_manifest_live.txt \
| xargs --max-args=1 -I {} \
  curl  --header "Accept-Encoding: gzip,deflate" \
        --write-out "%{size_download} %{size_header} %{http_code} %{url_effective}\n"  \
        --output /dev/null \
        --silent {} \
| awk '
    {
        sum = sum + $1 + $2 
        printf $1 "\t" $2 "\t" $1+$2 "\t" 
        printf("%.1f", ($1+$2)/1024)
        printf "\t" $3 "\t" $4 "\n"
    } 
    END {
        printf "\nTotal page transfer weight including headers: "
        printf("%d bytes, ", sum)
        printf("%.0f KB, ", sum/1024)
        printf("%.2f MB ", sum/1048576)
        printf("\nDesired size is: %d bytes", 1024 * 1024)
        printf("\nShortfall is:    %d bytes\n", 1024 * 1024 - sum)
    }
'
