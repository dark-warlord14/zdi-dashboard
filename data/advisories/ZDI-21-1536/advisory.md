# ZDI-21-1536: Trend Micro Maximum Security Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1536
- **ZDI-CAN:** ZDI-CAN-14587
- **Date:** 2021-12-14
- **CVE:** CVE-2021-44023
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1536/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Platinum Host Service. By creating a symbolic link, an attacker can abuse the service to overwrite a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-10867

## Disclosure Timeline

- 2021-07-13 - Vulnerability reported to vendor
- 2021-12-14 - Coordinated public release of advisory
