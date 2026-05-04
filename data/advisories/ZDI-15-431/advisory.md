# ZDI-15-431: Moxa SoftCMS IPCam.IPCam_Video_Render_Plugin.1 IVLCControl setRecordPrefix Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-431
- **ZDI-CAN:** ZDI-CAN-2955
- **Date:** 2015-09-08
- **CVE:** CVE-2015-6457
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Moxa
- **Affected Products:** SoftCMS
- **Credit:** Carsten Eiram - Risk Based Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-431/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Moxa SoftCMS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the setRecordPrefix method of the IPCam.IPCamVideoRender_Plugin.1 control. The implementation copies the user-supplied string to a field in a heap-based buffer without validating its size, which can lead to a heap buffer overflow. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-239-01

## Disclosure Timeline

- 2015-05-26 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
