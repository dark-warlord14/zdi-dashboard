# ZDI-17-225: Trend Micro InterScan Web Security Virtual Appliance uihelper Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-225
- **ZDI-CAN:** ZDI-CAN-4385
- **Date:** 2017-03-30
- **CVE:** N/A
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-225/
## Vulnerability Details

This vulnerability allows attackers to escalate privileges on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the uihelper application. The issue lies in the default configuration that allows the iscan user to execute commands under different privileges. An attacker can leverage this flaw in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2017-01-05 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
