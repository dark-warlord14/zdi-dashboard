# ZDI-18-471: Advantech WebAccess NMS DownloadAction Servlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-471
- **ZDI-CAN:** ZDI-CAN-5477
- **Date:** 2018-05-18
- **CVE:** CVE-2018-7503
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-471/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech WebAccess NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DownloadAction servlet. When parsing the filename and taskname parameters, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2017-12-08 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-05-18 - Advisory Updated
