# ZDI-15-096: Hewlett-Packard POS Printer Windows and OPOS Drivers OPOSPOSPrinter.ocx Open Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-096
- **ZDI-CAN:** ZDI-CAN-2506
- **Date:** 2015-03-12
- **CVE:** CVE-2014-7894
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** POS Printer Windows and OPOS Drivers
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard POS Printer Windows and OPOS Drivers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Open method in OPOSPOSPrinter.ocx. By supplying an overly long string to this method, an attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04583185

## Disclosure Timeline

- 2014-09-03 - Vulnerability reported to vendor
- 2015-03-12 - Coordinated public release of advisory
