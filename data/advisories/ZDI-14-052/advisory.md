# ZDI-14-052: Splunk collect file Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-052
- **ZDI-CAN:** ZDI-CAN-1864
- **Date:** 2014-04-03
- **CVE:** CVE-2013-6771
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Splunk
- **Affected Products:** Splunk Enterprise
- **Credit:** CyberCrown Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-052/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Splunk. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the advanced search functionality. Using a multi-staged attack, it is possible to execute arbitrary commands on the underlying operating system by leveraging a directory traversal flaw in the "file" parameter of the "collect" script. This vulnerability allows an attacker to execute code under the context of the process.

## Additional Details

Splunk has issued an update to correct this vulnerability. More details can be found at: http://www.splunk.com/view/SP-CAAAH76

## Disclosure Timeline

- 2013-08-09 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
