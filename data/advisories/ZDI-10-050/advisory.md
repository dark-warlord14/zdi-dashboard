# ZDI-10-050: Mozilla Firefox nsTreeSelection EventListener Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-050
- **ZDI-CAN:** ZDI-CAN-669
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0175
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.5.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on software utilizing a vulnerable version of Mozilla's Firefox. User interaction is required in that the victim must visit a malicious website or be coerced into opening a malicious document. The specific flaw exists within how the application handles particular events for an nsTreeSelection element. Upon execution of a "select" event the application will access an element without checking to see if it's been previously freed or not. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-17.html

## Disclosure Timeline

- 2010-01-15 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
