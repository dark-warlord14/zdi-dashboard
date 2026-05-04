# ZDI-22-014: Trend Micro Apex One Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-014
- **ZDI-CAN:** ZDI-CAN-13364
- **Date:** 2022-01-06
- **CVE:** CVE-2021-44024
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-014/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Real-time Scan Service. By creating a symbolic link, an attacker can abuse the service to overwrite a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289996

## Disclosure Timeline

- 2021-06-16 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
