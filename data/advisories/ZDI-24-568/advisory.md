# ZDI-24-568: Trend Micro Apex One Damage Cleanup Engine Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-568
- **ZDI-CAN:** ZDI-CAN-22038
- **Date:** 2024-06-06
- **CVE:** CVE-2024-36306
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-568/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Damage Cleanup Engine, which runs within the Trend Micro Common Client Real-time Scan Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000298063?language=en_US

## Disclosure Timeline

- 2023-10-03 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
