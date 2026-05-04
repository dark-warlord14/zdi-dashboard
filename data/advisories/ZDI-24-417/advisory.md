# ZDI-24-417: Xiaomi Pro 13 isUrlMatchLevel Permissive List of Allowed Inputs Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-417
- **ZDI-CAN:** ZDI-CAN-22559
- **Date:** 2024-05-01
- **CVE:** CVE-2023-26322
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Pro 13
- **Credit:** Team Orca of Sea Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-417/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Xiaomi Pro 13 smartphones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the isUrlMatchLevel method. The issue results from a permissive list of allowed inputs. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Xiaomi has issued an update to correct this vulnerability. More details can be found at: https://trust.mi.com/misrc/bulletins/advisory?cveId=542

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-05-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
