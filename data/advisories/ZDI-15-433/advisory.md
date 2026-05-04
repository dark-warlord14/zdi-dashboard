# ZDI-15-433: Moxa SoftCMS RTSPVIDEO.rtspvideoCtrl.1 AudioRecord Method ip Argument Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-433
- **ZDI-CAN:** ZDI-CAN-2952
- **Date:** 2015-09-08
- **CVE:** CVE-2015-6458
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Moxa
- **Affected Products:** SoftCMS
- **Credit:** Carsten Eiram - Risk Based Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-433/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Moxa SoftCMS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AudioRecord method in the RTSPVIDEO ActiveX control. The implementation copies the user-supplied string for the ip parameter to a fixed-size stack buffer without validating its size, which can lead to a stack buffer overflow. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-239-01

## Disclosure Timeline

- 2015-05-28 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
