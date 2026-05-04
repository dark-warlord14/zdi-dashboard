# ZDI-19-989: Symantec Endpoint Protection Manager LuComServer stDisScriptEngine Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-989
- **ZDI-CAN:** ZDI-CAN-9303
- **Date:** 2019-11-14
- **CVE:** CVE-2019-12759
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-989/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Symantec Endpoint Protection Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the stDisScriptEngine class within LuComServer. By invoking a method of this class, an attacker can launch an arbitrary executable. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: https://support.symantec.com/us/en/article.SYMSA1488.html

## Disclosure Timeline

- 2019-09-17 - Vulnerability reported to vendor
- 2019-11-14 - Coordinated public release of advisory
