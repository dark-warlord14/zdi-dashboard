# ZDI-24-1041: Google Chrome Updater DosDevices Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1041
- **ZDI-CAN:** ZDI-CAN-20781
- **Date:** 2024-08-01
- **CVE:** CVE-2023-7261
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Nassim Asrir
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1041/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Google Chrome. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the update mechanism. By creating a DOS device redirection, an attacker can abuse the update mechanism to launch an executable from an untrusted location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://issues.chromium.org/issues/40064602

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2024-08-01 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
