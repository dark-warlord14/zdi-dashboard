# ZDI-06-006: Symantec VERITAS NetBackup Database Manager Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-006
- **ZDI-CAN:** ZDI-CAN-016
- **Date:** 2006-03-27
- **CVE:** CVE-2006-0990
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas NetBackup
- **Credit:** Sebastian Apelt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable Symantec VERITAS NetBackup installations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetBackup Database Manager service (bpdbm.exe) due to insufficient bounds checking during a call to sprintf() that copies user-supplied data to a stack-based buffer. The vulnerable daemon listens on TCP port 13721.

## Additional Details

Symantec engineers have addressed these issues in all currently supported versions of NetBackup. Symantec engineers did additional reviews and will continue on-going reviews of related file functionality to further enhance the overall security of Veritas NetBackup products and to eliminate any additional potential concerns. Security updates are available for all supported products. Symantec strongly recommends all customers immediately apply the latest cumulative Security Pack updates or Maintenance Pack releases as indicated for their supported product versions to protect against threats of this nature. http://support.veritas.com/docs/281521

## Disclosure Timeline

- 2006-01-24 - Vulnerability reported to vendor
- 2006-03-27 - Coordinated public release of advisory
