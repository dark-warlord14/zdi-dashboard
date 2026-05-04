# ZDI-21-1052: Trend Micro Maximum Security Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1052
- **ZDI-CAN:** ZDI-CAN-13371
- **Date:** 2021-08-30
- **CVE:** CVE-2021-36744
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1052/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Maximum Security Agent. By creating a directory junction, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-10568

## Disclosure Timeline

- 2021-04-28 - Vulnerability reported to vendor
- 2021-08-30 - Coordinated public release of advisory
