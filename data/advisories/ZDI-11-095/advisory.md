# ZDI-11-095: Apple Webkit Error Message Mutation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-095
- **ZDI-CAN:** ZDI-CAN-982
- **Date:** 2011-03-02
- **CVE:** CVE-2010-1824
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-095/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the methodology the application takes to inform a user about an error while parsing a malformed document. When displaying the error message, the application will append the message to the current instance of the DOM tree causing another element to be removed which will lead to the styles being recalculated. When the styles are recalculated the application will access the initially freed element which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4554

## Disclosure Timeline

- 2010-10-18 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory
