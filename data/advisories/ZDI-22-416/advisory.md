# ZDI-22-416: (Pwn2Own) Cisco RV340 NGINX Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-416
- **ZDI-CAN:** ZDI-CAN-15892
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20709 , CVE-2022-20711
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Q. Kaiser from IoT Inspector Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-416/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Cisco RV340 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the NGINX web server. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored web session tokens, leading to further compromise.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2022-02-08 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
