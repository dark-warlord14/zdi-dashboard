# ZDI-11-118: Novell ZENworks Asset Management Path Traversal File Overwrite Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-118
- **ZDI-CAN:** ZDI-CAN-986
- **Date:** 2011-04-11
- **CVE:** CVE-2010-4229
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-118/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks Asset Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within a servlet provided within the Novell Zenworks distribution for uploading files. When processing the path name for the file, the servlet will allow a user to inject path traversal entities into the filename. Then, when the servlet downloads the provided file, the destination will store it to the user-provided location. This can lead to code execution under the context of the service.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=7007841&sliceId=1&docTypeID=DT_TID_1_1&dialogID=225674863&stateId=0%200%20225670765

## Disclosure Timeline

- 2010-11-30 - Vulnerability reported to vendor
- 2011-04-11 - Coordinated public release of advisory
