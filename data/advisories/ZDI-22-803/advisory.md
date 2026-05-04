# ZDI-22-803: Cisco RV340 JSON RPC set-snmp Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-803
- **ZDI-CAN:** ZDI-CAN-15636
- **Date:** 2022-05-27
- **CVE:** CVE-2022-20753
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-803/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of set-snmp JSON RPC requests. When parsing the usmUserPrivKey parameter, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sbrv-rce-OYLQbL9u

## Disclosure Timeline

- 2022-01-12 - Vulnerability reported to vendor
- 2022-05-27 - Coordinated public release of advisory
