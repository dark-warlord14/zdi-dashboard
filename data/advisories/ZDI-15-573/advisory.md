# ZDI-15-573: Unitronics VisiLogic OPLC IDE TeeCommander.ITeeCommander ActiveX Control ChartLink Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-573
- **ZDI-CAN:** ZDI-CAN-2904
- **Date:** 2015-12-02
- **CVE:** CVE-2015-6478
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Unitronics
- **Affected Products:** VisiLogic OPLC IDE
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-573/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Unitronics VisiLogic OPLC IDE . User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TeeCommander object in TeeChart5.ocx. A call to the ChartLink method of this object can cause arbitrary memory to be interpreted as an object. An attacker can leverage this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Unitronics has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-274-02

## Disclosure Timeline

- 2015-04-30 - Vulnerability reported to vendor
- 2015-12-02 - Coordinated public release of advisory
