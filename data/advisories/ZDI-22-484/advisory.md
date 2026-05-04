# ZDI-22-484: Bitdefender Total Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-484
- **ZDI-CAN:** ZDI-CAN-15206
- **Date:** 2022-03-09
- **CVE:** CVE-2021-4199
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bitdefender
- **Affected Products:** Total Security
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-484/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Bitdefender Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Bitdefender Auxiliary Service. By creating a symbolic link, an attacker can abuse the service to overwrite a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Bitdefender has issued an update to correct this vulnerability. More details can be found at: https://www.bitdefender.com/support/security-advisories/messaging_ipc-dll-null-pointer-dereference-in-multiple-bitdefender-products-va-10017/

## Disclosure Timeline

- 2021-09-08 - Vulnerability reported to vendor
- 2022-03-09 - Coordinated public release of advisory
