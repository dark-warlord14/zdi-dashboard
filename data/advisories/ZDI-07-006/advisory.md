# ZDI-07-006: Citrix Metaframe Presentation Server Print Provider Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-006
- **ZDI-CAN:** ZDI-CAN-101
- **Date:** 2007-01-24
- **CVE:** CVE-2007-0444
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Citrix, Citrix, Citrix
- **Affected Products:** MetaFrame Presentation Server, MetaFrame XP, Presentation Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of Citrix Presentation Server, Metaframe Presentation Server or MetaFrame XP. Authentication is not required to exploit this vulnerability. The specific flaw exists in a print provider installed by the Presentation Server. The cpprov.dll library doesn't properly handle certain invalid calls to the EnumPrintersW() and OpenPrinter() functions. For example, passing a string of 130 or more characters in the first argument to the OpenPrinter() function results in a stack-based buffer overflow and can be leveraged to execute code in the context of the Spooler service, which runs as the privileged LocalSystem account.

## Disclosure Timeline

- 2006-10-02 - Vulnerability reported to vendor
- 2007-01-24 - Coordinated public release of advisory
