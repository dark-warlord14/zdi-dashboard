# ZDI-12-106: Avaya IP Office Customer Call Reporter ImageUpload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-106
- **ZDI-CAN:** ZDI-CAN-1355
- **Date:** 2012-06-28
- **CVE:** CVE-2012-3811
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Avaya
- **Affected Products:** IP Office
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-106/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Avaya IP Office Customer Call Reporter. Authentication is not required to exploit this vulnerability. The specific flaw exists because Avaya IP Office Customer Call Reporter allows unauthenticated users to upload files to the webserver through ImageUpload.ashx. The uploaded files will not be stripped of their file extensions and the directory where they are uploaded to has no scripting restrictions. This flaw can lead the remote code execution under the context of the user running the IP Office Customer Call Reporter, usually NETWORK SERVICE.

## Additional Details

Avaya has issued an update to correct this vulnerability. More details can be found at: https://downloads.avaya.com/css/P8/documents/100164021

## Disclosure Timeline

- 2011-11-22 - Vulnerability reported to vendor
- 2012-06-28 - Coordinated public release of advisory
