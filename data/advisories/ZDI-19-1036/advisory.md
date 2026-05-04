# ZDI-19-1036: Hewlett Packard Enterprise Intelligent Management Center AccessMgrServlet className Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1036
- **ZDI-CAN:** ZDI-CAN-8928
- **Date:** 2020-01-29
- **CVE:** CVE-2020-24648
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Dusan Stevanovic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is required to exploit this vulnerability. The specific flaw exists within the transformEntity method of the MgrReqMsg class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=a00093539en_us

## Disclosure Timeline

- 2019-06-26 - Vulnerability reported to vendor
- 2020-01-29 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
