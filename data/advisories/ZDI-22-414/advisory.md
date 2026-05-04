# ZDI-22-414: (Pwn2Own) Cisco RV340 SSLVPN Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-414
- **ZDI-CAN:** ZDI-CAN-15784
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20699
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Flashback Team: Pedro Ribeiro (@pedrib1337) && Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-414/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SSL VPN service, which listens on TCP port 8443 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
