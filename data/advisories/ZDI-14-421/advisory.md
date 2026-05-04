# ZDI-14-421: ManageEngine Password Manager Pro UploadAccountActivities filename Directory Traversal Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-421
- **ZDI-CAN:** ZDI-CAN-2473
- **Date:** 2014-12-11
- **CVE:** CVE-2014-9372
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:P
- **Affected Vendors:** ManageEngine
- **Affected Products:** Password Manager Pro
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-421/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of ManageEngine Password Manager Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UploadAccountActivities servlet. The issue lies in the failure to properly sanitize a filename. A remote attacker can exploit this vulnerability to delete files from the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: http://www.manageengine.com/products/passwordmanagerpro/release-notes.html

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2014-12-11 - Coordinated public release of advisory
