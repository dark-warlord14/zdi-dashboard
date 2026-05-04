# ZDI-19-1025: Trend Micro Maximum Security Link Resolution Information Disclosure And Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1025
- **ZDI-CAN:** ZDI-CAN-9391
- **Date:** 2019-12-19
- **CVE:** CVE-2019-19693
- **CVSS:** 7.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Nabeel Ahmed (@rogue_kdc)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1025/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information or to create a denial-of-service condition on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of junctions. By creating a junction, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to disclose sensitive information or to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-us/home/pages/technical-support/1124043.aspx

## Disclosure Timeline

- 2019-10-17 - Vulnerability reported to vendor
- 2019-12-19 - Coordinated public release of advisory
