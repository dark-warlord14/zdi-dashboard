# ZDI-17-694: SpiderControl SCADA MicroBrowser StaticHTMLTagsFileName Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-694
- **ZDI-CAN:** ZDI-CAN-4194
- **Date:** 2017-08-23
- **CVE:** CVE-2017-12707
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SpiderControl
- **Affected Products:** SCADA MicroBrowser
- **Credit:** juushya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-694/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SpiderControl SCADA MicroBrowser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the StaticHTMLTagsFileName tag. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

SpiderControl has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-234-02

## Disclosure Timeline

- 2017-02-10 - Vulnerability reported to vendor
- 2017-08-23 - Coordinated public release of advisory
