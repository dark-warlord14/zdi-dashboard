# ZDI-15-244: Arcserve Unified Data Protection Management Service EdgeServiceImpl getBackupPolicies Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-244
- **ZDI-CAN:** ZDI-CAN-2866
- **Date:** 2015-05-26
- **CVE:** CVE-2015-4069
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Arcserve
- **Affected Products:** Unified Data Protection
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-244/
## Vulnerability Details

This vulnerability allows remote attackers to disclose information on vulnerable installations of Arcserve Unified Data Protection. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getBackupPolicies method of the EdgeServiceImpl web service. By sending a crafted SOAP request, this method will return an individual application's backup policies which contains sensitive credentials. An attacker could use this to create an information disclosure under the context of the SYSTEM user.

## Additional Details

Arcserve has issued an update to correct this vulnerability. More details can be found at: http://documentation.arcserve.com/Arcserve-UDP/Available/V5/ENU/Bookshelf_Files/HTML/Update%204/UDP_Update4_ReleaseNotes.html

## Disclosure Timeline

- 2015-04-09 - Vulnerability reported to vendor
- 2015-05-26 - Coordinated public release of advisory
