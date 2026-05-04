# ZDI-18-966: Hewlett Packard Enterprise Intelligent Management Center imciccdm createFabricAutoCfgFile Directory Traversal Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-966
- **ZDI-CAN:** ZDI-CAN-6109
- **Date:** 2018-08-31
- **CVE:** CVE-2018-7102
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:C/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-966/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the imciccdm component. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files under the context of Administrator.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=hpesbhf03887en_us

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-08-31 - Coordinated public release of advisory
- 2023-01-19 - Advisory Updated
