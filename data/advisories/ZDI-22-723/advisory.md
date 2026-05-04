# ZDI-22-723: Cisco RV340 JSON RPC set-snmp Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-723
- **ZDI-CAN:** ZDI-CAN-15633
- **Date:** 2022-05-09
- **CVE:** CVE-2022-20801
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-723/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of set-snmp JSON RPC requests. When parsing the usmUserPrivKey parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-rv-cmd-inj-8Pv9JMJD

## Disclosure Timeline

- 2022-01-07 - Vulnerability reported to vendor
- 2022-05-09 - Coordinated public release of advisory
