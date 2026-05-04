# ZDI-20-228: Symantec Endpoint Protection AvHostPlugin Missing Authentication Arbitrary File Move Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-228
- **ZDI-CAN:** ZDI-CAN-9397
- **Date:** 2020-02-11
- **CVE:** CVE-2020-5825
- **CVSS:** 7.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-228/
## Vulnerability Details

This vulnerability allows local attackers to move arbitrary files on affected installations of Symantec Endpoint Protection. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AvHostPlugin.dll module. By invoking a method of a COM class, an attacker can move arbitrary files. An attacker can leverage this vulnerability to create a denial-of-service condition on the system. An attacker can also leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: https://support.symantec.com/us/en/article.SYMSA1505.html

## Disclosure Timeline

- 2019-10-29 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
