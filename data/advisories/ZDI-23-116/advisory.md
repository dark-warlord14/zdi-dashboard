# ZDI-23-116: VMware vRealize Log Insight getConfig Missing Authentication for Critical Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-116
- **ZDI-CAN:** ZDI-CAN-17964
- **Date:** 2023-02-09
- **CVE:** CVE-2022-31711
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** vRealize
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-116/
## Vulnerability Details

This vulnerability allows remote attackers to disclose information on affected installations of VMware vRealize Log Insight. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getConfig function. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0001.html

## Disclosure Timeline

- 2022-09-02 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
