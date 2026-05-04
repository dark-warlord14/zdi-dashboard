# ZDI-19-667: Oracle VirtualBox WINED3DSIH_TEX Opcode Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-667
- **ZDI-CAN:** ZDI-CAN-8417
- **Date:** 2019-07-22
- **CVE:** CVE-2019-2866
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** huyna of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-667/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of the WINED3DSIH_TEX opcode. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujul2019-5072835.html

## Disclosure Timeline

- 2019-05-29 - Vulnerability reported to vendor
- 2019-07-22 - Coordinated public release of advisory
