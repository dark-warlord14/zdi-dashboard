# ZDI-25-241: Trend Micro Deep Security Agent Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-241
- **ZDI-CAN:** ZDI-CAN-25681
- **Date:** 2025-04-09
- **CVE:** CVE-2025-30642
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Security
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-241/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Deep Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Damage Cleanup Engine. By creating a junction, an attacker can abuse this component to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019344

## Disclosure Timeline

- 2024-12-19 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
