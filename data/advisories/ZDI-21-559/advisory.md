# ZDI-21-559: Cisco RV340 set_snmp usmUserPrivKey Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-559
- **ZDI-CAN:** ZDI-CAN-11798
- **Date:** 2021-05-11
- **CVE:** CVE-2021-1414
- **CVSS:** 5.5
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** T Shiomitsu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-559/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of JSON-RPC requests. When parsing the usmUserPrivKey property, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sb-rv34x-rce-8bfG2h6b

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-05-11 - Coordinated public release of advisory
