# ZDI-24-571: Trend Micro Apex One Security Agent Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-571
- **ZDI-CAN:** ZDI-CAN-22667
- **Date:** 2024-06-06
- **CVE:** CVE-2024-36304
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lays (@_L4ys) of TRAPA Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-571/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT RealTime Scan service. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000298063?language=en_US

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
