# ZDI-06-044: Adobe Download Manager AOM Parsing Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-044
- **ZDI-CAN:** ZDI-CAN-042
- **Date:** 2006-12-06
- **CVE:** CVE-2006-5856
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Download Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Download Manager application. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the AOM file format parser. A long [URL] element inside of a [DownloadRecord] element within an AOM file will result in a stack-based buffer overflow condition leading to execution of arbitrary code. The Download Manager is installed during the installation of of other Adobe products, such as Acrobat Reader. When installed, the download manager becomes the default application to handle .AOM files.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/go/apsb06-19/

## Disclosure Timeline

- 2006-04-07 - Vulnerability reported to vendor
- 2006-12-06 - Coordinated public release of advisory
