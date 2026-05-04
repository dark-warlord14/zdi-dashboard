# ZDI-18-955: Hewlett Packard Enterprise Intelligent Management Center TFTP deleteBaseCfgfile Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-955
- **ZDI-CAN:** ZDI-CAN-6110
- **Date:** 2018-08-30
- **CVE:** CVE-2018-7092
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-955/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TFTP server. The issue results from the lack of proper validation of user-supplied data, which can allow for the deletion of arbitrary files. An attacker can leverage this vulnerability to delete any files accessible to the Administrator user.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03872en_us

## Disclosure Timeline

- 2018-04-19 - Vulnerability reported to vendor
- 2018-08-30 - Coordinated public release of advisory
- 2018-08-30 - Advisory Updated
