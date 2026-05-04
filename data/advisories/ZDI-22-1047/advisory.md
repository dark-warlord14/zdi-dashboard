# ZDI-22-1047: Cisco RV340 wfapp Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1047
- **ZDI-CAN:** ZDI-CAN-15984
- **Date:** 2022-08-04
- **CVE:** CVE-2022-20827
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Q. Kaiser from IoT Inspector Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1047/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the wfapp application. A crafted server response can trigger execution of a system call composed from a attacker-supplied string. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sb-mult-vuln-CbVp4SUR

## Disclosure Timeline

- 2022-04-13 - Vulnerability reported to vendor
- 2022-08-04 - Coordinated public release of advisory
