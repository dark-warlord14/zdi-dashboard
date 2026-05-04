# ZDI-20-217: Symantec Endpoint Protection AvHostPlugin Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-217
- **ZDI-CAN:** ZDI-CAN-9420
- **Date:** 2020-02-11
- **CVE:** CVE-2020-5820
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-217/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Symantec Endpoint Protection. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AvHostPlugin.dll. The issue results from the lack of proper validation of user-supplied data, which can result in a write before the start of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: https://support.symantec.com/us/en/article.SYMSA1505.html

## Disclosure Timeline

- 2019-10-01 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
