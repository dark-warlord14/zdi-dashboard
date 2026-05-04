# ZDI-19-990: Symantec Endpoint Protection Manager OpenSSL Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-990
- **ZDI-CAN:** ZDI-CAN-9477
- **Date:** 2019-11-14
- **CVE:** CVE-2019-18372
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** gweeperx
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-990/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Symantec Endpoint Protection Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. When processing an HTTPS request, the process loads the OpenSSL configuration file, which can be used to load arbitrary executable files. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the NT SERVICE\semwebsrv user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: https://support.symantec.com/us/en/article.SYMSA1488.html

## Disclosure Timeline

- 2019-10-17 - Vulnerability reported to vendor
- 2019-11-14 - Coordinated public release of advisory
- 2021-01-05 - Advisory Updated
