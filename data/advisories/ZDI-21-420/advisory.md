# ZDI-21-420: Trend Micro Antivirus for Mac Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-420
- **ZDI-CAN:** ZDI-CAN-12217
- **Date:** 2021-04-15
- **CVE:** CVE-2021-28648
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Antivirus for Mac
- **Credit:** Wojciech Regula
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-420/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Antivirus for Mac. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within com.trendmicro.AFM.HelperTool. The issue results from improper access control. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-10293

## Disclosure Timeline

- 2021-01-08 - Vulnerability reported to vendor
- 2021-04-15 - Coordinated public release of advisory
