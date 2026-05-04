# ZDI-23-651: Trend Micro Apex One Security Agent Link Following Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-651
- **ZDI-CAN:** ZDI-CAN-16525
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32556
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-651/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the NT Apex One RealTime Scan Service. By creating a mount point, an attacker can abuse the service to disclose the contents of a file. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000293108?language=en_US

## Disclosure Timeline

- 2022-04-13 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
