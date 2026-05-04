# ZDI-25-227: (Pwn2Own) Samsung Galaxy S24 Gaming Hub Exposed Dangerous Method Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-227
- **ZDI-CAN:** ZDI-CAN-25648
- **Date:** 2025-04-09
- **CVE:** CVE-2024-49420
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S24
- **Credit:** Ken Gannon of NCC Group (@yogehi)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-227/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Samsung Galaxy S24. An attacker must first obtain the ability to execute low-privileged script on the target system in order to exploit this vulnerability. The specific flaw exists within the Gaming Hub application. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to escalate privileges and perform actions in the context of the user.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2024&month=12

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
