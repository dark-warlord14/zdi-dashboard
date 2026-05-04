# ZDI-20-675: Trend Micro InterScan Web Security Virtual Appliance Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-675
- **ZDI-CAN:** ZDI-CAN-10088
- **Date:** 2020-05-27
- **CVE:** CVE-2020-8603
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Mehmet INCE (@mdisec)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-675/
## Vulnerability Details

This vulnerability allows remote attackers to tamper with the web interface of affected installations of Trend Micro InterScan Web Security Virtual Appliance. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of logged URLs. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

https://success.trendmicro.com/solution/000253095

## Disclosure Timeline

- 2020-01-17 - Vulnerability reported to vendor
- 2020-05-27 - Coordinated public release of advisory
- 2020-05-28 - Advisory Updated
