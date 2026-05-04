# ZDI-22-1404: Trend Micro Apex One Vulnerability Protection Service Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1404
- **ZDI-CAN:** ZDI-CAN-16518
- **Date:** 2022-10-07
- **CVE:** CVE-2022-41744
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1404/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One Vulnerability Protection Service. The issue results from the lack of proper locking when performing operations on a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000291645?language=en_US

## Disclosure Timeline

- 2022-08-19 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory
