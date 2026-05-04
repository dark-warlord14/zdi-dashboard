# ZDI-21-683: Arlo Q Plus SSH Use of Hard-coded Credentials Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-683
- **ZDI-CAN:** ZDI-CAN-12890
- **Date:** 2021-06-14
- **CVE:** CVE-2021-31505
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Arlo
- **Affected Products:** Q Plus
- **Credit:** Team FLASHBACK: Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) + Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-683/
## Vulnerability Details

This vulnerability allows attackers with physical access to escalate privileges on affected installations of Arlo Q Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SSH service. The device can be booted into a special operation mode where hard-coded credentials are accepted for SSH authentication. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Arlo has issued an update to correct this vulnerability. More details can be found at: https://kb.arlo.com/000062592/Security-Advisory-for-Arlo-Q-Plus-SSH-Use-of-Hard-coded-Credentials-Allowing-Privilege-Escalation

## Disclosure Timeline

- 2021-02-12 - Vulnerability reported to vendor
- 2021-06-14 - Coordinated public release of advisory
