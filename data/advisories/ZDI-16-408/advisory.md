# ZDI-16-408: Eaton ELCSoft Heap Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-408
- **ZDI-CAN:** ZDI-CAN-3675
- **Date:** 2016-07-07
- **CVE:** CVE-2016-4509
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Eaton
- **Affected Products:** ELCSoft
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-408/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Eaton ELCSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of EPC files. Parsing a specially crafted EPC file can cause ELCSoft.exe to overwrite a TList object in memory. An attacker can leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Eaton has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-182-01

## Disclosure Timeline

- 2016-04-07 - Vulnerability reported to vendor
- 2016-07-07 - Coordinated public release of advisory
