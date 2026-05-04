# ZDI-15-241: Arcserve Unified Data Protection Management Service reportFileServlet Directory Traversal Information Disclosure and Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-241
- **ZDI-CAN:** ZDI-CAN-2809
- **Date:** 2015-05-26
- **CVE:** CVE-2015-4068
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:C
- **Affected Vendors:** Arcserve
- **Affected Products:** Unified Data Protection
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-241/
## Vulnerability Details

This vulnerability allows remote attackers to disclose and delete files on vulnerable installations of Arcserve Unified Data Protection. Authentication is not required to exploit this vulnerability. The specific flaw exists within the reportFileServlet. The issue lies in the failure to sanitize the path of files requested. An attacker could use this to create an information disclosure and denial-of-service condition under the context of the SYSTEM user.

## Additional Details

Arcserve has issued an update to correct this vulnerability. More details can be found at: http://documentation.arcserve.com/Arcserve-UDP/Available/V5/ENU/Bookshelf_Files/HTML/Update%204/UDP_Update4_ReleaseNotes.html

## Disclosure Timeline

- 2015-04-03 - Vulnerability reported to vendor
- 2015-05-26 - Coordinated public release of advisory
