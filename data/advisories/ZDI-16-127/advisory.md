# ZDI-16-127: Advantech WebAccess Dashboard Viewer FileUploadHandler Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-127
- **ZDI-CAN:** ZDI-CAN-3127
- **Date:** 2016-02-05
- **CVE:** CVE-2016-0854
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WebAccess Dashboard Viewer. Insufficient validation within the FileUpload script allows unauthenticated callers to upload arbitrary code to directories in the server where the code can be automatically executed under the high-privilege context of the IIS AppPool. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-014-01

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2016-02-05 - Coordinated public release of advisory
