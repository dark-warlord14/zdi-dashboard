# ZDI-17-227: Trend Micro InterScan Web Security Virtual Appliance ConfigBackup Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-227
- **ZDI-CAN:** ZDI-CAN-4262
- **Date:** 2017-03-30
- **CVE:** N/A
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-227/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within processing of the ConfigBackup servlet. A low-privilege user can perform actions that should require extra privileges. An attacker can leverage this vulnerability to disclose sensitive information under the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
