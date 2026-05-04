# ZDI-20-218: Symantec Endpoint Protection ccSvc Missing Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-218
- **ZDI-CAN:** ZDI-CAN-9426
- **Date:** 2020-02-11
- **CVE:** CVE-2020-5822
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-218/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Symantec Endpoint Protection. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ccSvc.dll module. By invoking a method of a COM class, an attacker can launch an arbitrary executable. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: https://support.symantec.com/us/en/article.SYMSA1505.html

## Disclosure Timeline

- 2019-10-08 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
